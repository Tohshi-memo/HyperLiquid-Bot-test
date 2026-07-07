# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T22:23:05.645519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.292` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `0.0396` n `229`; crypto_major avg `0.063` n `8`; equity avg `0.079` n `91`; fx avg `0.0089` n `6`; index avg `-0.01` n `25`; metal avg `0.0126` n `20`; unknown avg `-0.0009` n `763`
- 1h: commodity avg `-0.0739` n `12`; crypto_alt avg `-0.3834` n `229`; crypto_major avg `-0.1028` n `8`; equity avg `-0.167` n `91`; fx avg `-0.0037` n `6`; index avg `-0.0207` n `25`; metal avg `-0.0569` n `20`; unknown avg `-0.05` n `763`
- 4h: commodity avg `0.4831` n `12`; crypto_alt avg `-1.6662` n `229`; crypto_major avg `-1.4401` n `8`; equity avg `-0.8874` n `91`; fx avg `0.0002` n `6`; index avg `-0.1481` n `25`; metal avg `-0.4712` n `20`; unknown avg `0.7157` n `761`
- 24h: commodity avg `0.9391` n `12`; crypto_alt avg `-3.1795` n `229`; crypto_major avg `-2.2337` n `8`; equity avg `-3.5753` n `91`; fx avg `-0.267` n `6`; index avg `-0.6736` n `25`; metal avg `-0.6662` n `20`; unknown avg `-0.3974` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
