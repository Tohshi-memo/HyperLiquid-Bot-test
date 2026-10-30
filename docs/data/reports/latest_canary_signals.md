# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T16:07:30.580270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0471` n `13`; crypto_alt avg `0.1314` n `238`; crypto_major avg `-0.0532` n `8`; equity avg `-0.1992` n `156`; fx avg `0.0391` n `6`; index avg `-0.0228` n `27`; metal avg `0.009` n `20`; unknown avg `0.064` n `1249`
- 1h: commodity avg `0.1077` n `13`; crypto_alt avg `-0.2677` n `238`; crypto_major avg `-0.407` n `8`; equity avg `-0.7346` n `156`; fx avg `0.0591` n `6`; index avg `-0.0649` n `27`; metal avg `-0.0828` n `20`; unknown avg `0.4766` n `1247`
- 4h: commodity avg `0.0543` n `13`; crypto_alt avg `0.1873` n `238`; crypto_major avg `-0.1946` n `8`; equity avg `-1.4724` n `156`; fx avg `-0.0391` n `6`; index avg `-0.0787` n `27`; metal avg `-0.2464` n `20`; unknown avg `4.516` n `1149`
- 24h: commodity avg `0.5948` n `13`; crypto_alt avg `-6.1421` n `238`; crypto_major avg `-5.1309` n `8`; equity avg `-6.237` n `156`; fx avg `-0.0872` n `6`; index avg `-0.5237` n `27`; metal avg `-0.9578` n `20`; unknown avg `45.7246` n `1038`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1678`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1448`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
