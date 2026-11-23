# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T23:22:32.953402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0225` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0259` n `13`; crypto_alt avg `0.182` n `239`; crypto_major avg `-0.0281` n `8`; equity avg `-0.1024` n `166`; fx avg `-0.0069` n `6`; index avg `-0.0104` n `27`; metal avg `-0.0491` n `20`; unknown avg `0.3802` n `1256`
- 1h: commodity avg `0.0106` n `13`; crypto_alt avg `0.1505` n `239`; crypto_major avg `-0.1786` n `8`; equity avg `0.0109` n `166`; fx avg `0.0116` n `6`; index avg `0.0068` n `27`; metal avg `0.0038` n `20`; unknown avg `3.4794` n `1256`
- 4h: commodity avg `0.1037` n `13`; crypto_alt avg `-1.2029` n `239`; crypto_major avg `-0.9984` n `8`; equity avg `0.1929` n `166`; fx avg `0.0156` n `6`; index avg `0.0241` n `27`; metal avg `-0.0878` n `20`; unknown avg `165.7642` n `1214`
- 24h: commodity avg `-1.0412` n `13`; crypto_alt avg `0.8319` n `239`; crypto_major avg `0.9294` n `8`; equity avg `6.0439` n `166`; fx avg `-0.1977` n `6`; index avg `0.6252` n `27`; metal avg `0.2177` n `20`; unknown avg `50.0201` n `1046`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
