# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T11:43:20.455439+00:00`
- Correlation status: `ready`
- Asset price records: `642`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.108` n `12`; crypto_alt avg `0.0014` n `228`; crypto_major avg `-0.0691` n `8`; equity avg `0.0785` n `65`; fx avg `0.0253` n `5`; index avg `-0.0009` n `23`; metal avg `0.0406` n `18`; unknown avg `0.0962` n `375`
- 1h: commodity avg `-0.0051` n `12`; crypto_alt avg `0.1002` n `228`; crypto_major avg `0.0224` n `8`; equity avg `-0.0161` n `65`; fx avg `-0.0086` n `5`; index avg `0.0598` n `23`; metal avg `-0.0888` n `18`; unknown avg `-0.003` n `375`
- 4h: commodity avg `0.0013` n `12`; crypto_alt avg `0.7904` n `228`; crypto_major avg `0.5173` n `8`; equity avg `0.5512` n `65`; fx avg `0.0393` n `5`; index avg `0.1739` n `23`; metal avg `0.3497` n `18`; unknown avg `0.7577` n `375`
- 24h: commodity avg `1.569` n `12`; crypto_alt avg `1.1104` n `228`; crypto_major avg `-1.3427` n `8`; equity avg `-0.5448` n `65`; fx avg `0.2658` n `5`; index avg `-0.3834` n `23`; metal avg `-0.5094` n `18`; unknown avg `-0.0998` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.134`, n `634`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1339`, n `634`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `638`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0927`, n `638`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `638`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0903`, n `638`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0893`, n `634`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.08`, n `634`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0788`, n `634`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0766`, n `638`, weak_sample_signal
