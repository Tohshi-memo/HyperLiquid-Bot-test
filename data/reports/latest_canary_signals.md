# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T15:07:31.226253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.022` n `12`; crypto_alt avg `-0.3048` n `234`; crypto_major avg `-0.3916` n `8`; equity avg `-0.2051` n `138`; fx avg `0.0032` n `6`; index avg `-0.0081` n `26`; metal avg `-0.0571` n `20`; unknown avg `0.328` n `917`
- 1h: commodity avg `0.0386` n `12`; crypto_alt avg `0.0067` n `234`; crypto_major avg `0.0209` n `8`; equity avg `0.2024` n `138`; fx avg `-0.0245` n `6`; index avg `0.0166` n `26`; metal avg `-0.1342` n `20`; unknown avg `1.3263` n `915`
- 4h: commodity avg `0.1089` n `12`; crypto_alt avg `0.2082` n `234`; crypto_major avg `0.6355` n `8`; equity avg `0.3625` n `138`; fx avg `-0.0404` n `6`; index avg `0.1097` n `26`; metal avg `0.172` n `20`; unknown avg `1.0502` n `891`
- 24h: commodity avg `-0.1409` n `12`; crypto_alt avg `4.0054` n `234`; crypto_major avg `2.1888` n `8`; equity avg `1.2372` n `138`; fx avg `0.0453` n `6`; index avg `0.1549` n `26`; metal avg `0.066` n `20`; unknown avg `0.7254` n `711`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
