# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T23:07:30.140534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.0349` n `230`; crypto_major avg `-0.0802` n `8`; equity avg `0.0914` n `92`; fx avg `-0.0189` n `6`; index avg `0.0186` n `25`; metal avg `0.0015` n `20`; unknown avg `0.0623` n `768`
- 1h: commodity avg `-0.0461` n `12`; crypto_alt avg `0.2599` n `230`; crypto_major avg `0.2753` n `8`; equity avg `0.122` n `92`; fx avg `-0.0153` n `6`; index avg `0.0316` n `25`; metal avg `-0.0372` n `20`; unknown avg `-0.1462` n `768`
- 4h: commodity avg `0.0395` n `12`; crypto_alt avg `0.2601` n `230`; crypto_major avg `0.2307` n `8`; equity avg `0.3488` n `92`; fx avg `-0.0132` n `6`; index avg `0.0537` n `25`; metal avg `-0.0123` n `20`; unknown avg `-0.1324` n `768`
- 24h: commodity avg `0.1585` n `12`; crypto_alt avg `2.6262` n `230`; crypto_major avg `4.0324` n `8`; equity avg `1.9322` n `92`; fx avg `0.0053` n `6`; index avg `0.4991` n `25`; metal avg `0.5541` n `20`; unknown avg `0.2683` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0561`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
