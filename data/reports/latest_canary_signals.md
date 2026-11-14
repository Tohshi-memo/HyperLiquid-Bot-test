# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T14:29:38.218329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8457` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.8167` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.1742` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0175` n `13`; crypto_alt avg `-0.9685` n `239`; crypto_major avg `-0.7231` n `8`; equity avg `-0.1331` n `162`; fx avg `0.0002` n `6`; index avg `-0.0085` n `27`; metal avg `-0.0246` n `20`; unknown avg `-0.1888` n `1256`
- 1h: commodity avg `0.0006` n `13`; crypto_alt avg `-1.6396` n `239`; crypto_major avg `-1.1881` n `8`; equity avg `-0.2638` n `162`; fx avg `-0.0019` n `6`; index avg `-0.0139` n `27`; metal avg `-0.0303` n `20`; unknown avg `158.9708` n `1254`
- 4h: commodity avg `-0.0354` n `13`; crypto_alt avg `-2.1526` n `239`; crypto_major avg `-1.872` n `8`; equity avg `-0.423` n `162`; fx avg `0.0131` n `6`; index avg `-0.0263` n `27`; metal avg `-0.0553` n `20`; unknown avg `40.9109` n `1240`
- 24h: commodity avg `-0.221` n `13`; crypto_alt avg `-6.1682` n `239`; crypto_major avg `-5.7967` n `8`; equity avg `-3.5266` n `162`; fx avg `-0.1153` n `6`; index avg `-0.2748` n `27`; metal avg `-0.2831` n `20`; unknown avg `0.6922` n `1096`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
