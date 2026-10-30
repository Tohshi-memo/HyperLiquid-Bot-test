# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T01:07:26.887481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4058` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0239` n `13`; crypto_alt avg `-0.266` n `238`; crypto_major avg `-0.1924` n `8`; equity avg `-0.4913` n `156`; fx avg `-0.013` n `6`; index avg `-0.0821` n `27`; metal avg `-0.2779` n `20`; unknown avg `4.4357` n `1254`
- 1h: commodity avg `-0.0628` n `13`; crypto_alt avg `-1.5648` n `238`; crypto_major avg `-0.7362` n `8`; equity avg `-1.0406` n `156`; fx avg `0.008` n `6`; index avg `-0.1452` n `27`; metal avg `-0.2031` n `20`; unknown avg `5.0523` n `1252`
- 4h: commodity avg `-0.0807` n `13`; crypto_alt avg `-3.1734` n `238`; crypto_major avg `-1.6145` n `8`; equity avg `-1.6887` n `156`; fx avg `0.0108` n `6`; index avg `-0.2087` n `27`; metal avg `-0.2927` n `20`; unknown avg `14.8263` n `1240`
- 24h: commodity avg `-0.276` n `13`; crypto_alt avg `-7.5426` n `238`; crypto_major avg `-3.1891` n `8`; equity avg `-4.5108` n `155`; fx avg `0.1852` n `6`; index avg `-0.4865` n `27`; metal avg `-0.8476` n `20`; unknown avg `33.2532` n `988`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
