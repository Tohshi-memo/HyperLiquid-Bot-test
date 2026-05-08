# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T21:22:12.685993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0155` n `12`; crypto_alt avg `-0.0225` n `228`; crypto_major avg `0.094` n `8`; equity avg `0.0492` n `65`; fx avg `-0.0185` n `5`; index avg `0.0108` n `23`; metal avg `-0.004` n `18`; unknown avg `-0.3942` n `375`
- 1h: commodity avg `0.0286` n `12`; crypto_alt avg `0.1292` n `228`; crypto_major avg `-0.0729` n `8`; equity avg `0.0475` n `65`; fx avg `-0.0211` n `5`; index avg `-0.0716` n `23`; metal avg `0.0388` n `18`; unknown avg `-0.1712` n `375`
- 4h: commodity avg `-0.3466` n `12`; crypto_alt avg `0.8791` n `228`; crypto_major avg `0.8573` n `8`; equity avg `1.0757` n `65`; fx avg `0.0284` n `5`; index avg `0.0512` n `23`; metal avg `0.0354` n `18`; unknown avg `-0.1254` n `375`
- 24h: commodity avg `-1.1466` n `12`; crypto_alt avg `3.6172` n `228`; crypto_major avg `1.5106` n `8`; equity avg `3.8149` n `65`; fx avg `0.2167` n `5`; index avg `1.4893` n `23`; metal avg `1.2506` n `18`; unknown avg `0.7415` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
