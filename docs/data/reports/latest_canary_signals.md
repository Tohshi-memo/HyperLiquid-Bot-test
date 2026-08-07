# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T21:51:52.324087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0788` n `12`; crypto_alt avg `-0.0631` n `230`; crypto_major avg `-0.0217` n `8`; equity avg `0.01` n `112`; fx avg `0.0016` n `6`; index avg `-0.0053` n `25`; metal avg `-0.0177` n `20`; unknown avg `-0.0385` n `782`
- 1h: commodity avg `-0.1031` n `12`; crypto_alt avg `-0.0766` n `230`; crypto_major avg `-0.0946` n `8`; equity avg `-0.0175` n `112`; fx avg `0.0169` n `6`; index avg `-0.0161` n `25`; metal avg `0.0357` n `20`; unknown avg `-0.0797` n `782`
- 4h: commodity avg `-0.321` n `12`; crypto_alt avg `-0.081` n `230`; crypto_major avg `0.3554` n `8`; equity avg `0.426` n `112`; fx avg `0.0131` n `6`; index avg `0.0523` n `25`; metal avg `0.0283` n `20`; unknown avg `-0.1614` n `782`
- 24h: commodity avg `-0.2608` n `12`; crypto_alt avg `-0.6544` n `230`; crypto_major avg `-0.1405` n `8`; equity avg `1.7406` n `112`; fx avg `-0.1185` n `6`; index avg `0.0953` n `25`; metal avg `0.428` n `20`; unknown avg `0.112` n `766`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
