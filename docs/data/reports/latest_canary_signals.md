# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T20:22:32.724268+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0225` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0274` n `13`; crypto_alt avg `0.3881` n `239`; crypto_major avg `0.245` n `8`; equity avg `0.0879` n `158`; fx avg `0.0073` n `6`; index avg `0.0214` n `27`; metal avg `0.0128` n `20`; unknown avg `0.4367` n `1264`
- 1h: commodity avg `0.2414` n `13`; crypto_alt avg `-0.0557` n `239`; crypto_major avg `-0.1148` n `8`; equity avg `-0.0742` n `158`; fx avg `0.026` n `6`; index avg `-0.0037` n `27`; metal avg `0.0361` n `20`; unknown avg `164.9274` n `1236`
- 4h: commodity avg `-0.5989` n `13`; crypto_alt avg `-1.2322` n `239`; crypto_major avg `-0.9626` n `8`; equity avg `0.221` n `158`; fx avg `0.0044` n `6`; index avg `0.0599` n `27`; metal avg `0.2491` n `20`; unknown avg `4.5815` n `1238`
- 24h: commodity avg `-1.7086` n `13`; crypto_alt avg `1.7792` n `239`; crypto_major avg `2.0984` n `8`; equity avg `-0.8947` n `158`; fx avg `0.071` n `6`; index avg `0.1349` n `27`; metal avg `1.3412` n `20`; unknown avg `0.2411` n `1117`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2629`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
