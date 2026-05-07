# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T15:37:25.212965+00:00`
- Correlation status: `ready`
- Asset price records: `562`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0464` n `12`; crypto_alt avg `0.4407` n `228`; crypto_major avg `0.1812` n `8`; equity avg `0.2043` n `65`; fx avg `0.0313` n `5`; index avg `0.0405` n `23`; metal avg `-0.2048` n `18`; unknown avg `0.1334` n `365`
- 1h: commodity avg `0.4614` n `12`; crypto_alt avg `0.2656` n `228`; crypto_major avg `0.0612` n `8`; equity avg `-0.206` n `65`; fx avg `0.0567` n `5`; index avg `0.0225` n `23`; metal avg `-0.2892` n `18`; unknown avg `-0.0635` n `365`
- 4h: commodity avg `0.341` n `12`; crypto_alt avg `-0.6776` n `228`; crypto_major avg `-1.178` n `8`; equity avg `-0.447` n `65`; fx avg `0.045` n `5`; index avg `-0.1901` n `23`; metal avg `-0.1382` n `18`; unknown avg `-0.1359` n `365`
- 24h: commodity avg `-0.6585` n `12`; crypto_alt avg `0.6215` n `228`; crypto_major avg `-1.7636` n `8`; equity avg `0.883` n `65`; fx avg `0.1539` n `5`; index avg `0.3755` n `23`; metal avg `1.4425` n `18`; unknown avg `-0.1187` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1346`, n `558`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1244`, n `558`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1087`, n `558`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0986`, n `558`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0925`, n `558`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.085`, n `554`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0844`, n `554`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0837`, n `554`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0799`, n `554`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0757`, n `558`, weak_sample_signal
