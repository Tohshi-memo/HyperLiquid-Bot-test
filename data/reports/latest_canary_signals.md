# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T08:52:35.572854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0181` n `13`; crypto_alt avg `0.055` n `235`; crypto_major avg `0.09` n `8`; equity avg `-0.0434` n `150`; fx avg `0.0227` n `6`; index avg `-0.0075` n `26`; metal avg `0.0241` n `20`; unknown avg `-0.0859` n `1077`
- 1h: commodity avg `0.0573` n `13`; crypto_alt avg `-0.1207` n `235`; crypto_major avg `-0.2282` n `8`; equity avg `-0.0523` n `150`; fx avg `0.0132` n `6`; index avg `0.005` n `26`; metal avg `0.0691` n `20`; unknown avg `2.1548` n `1059`
- 4h: commodity avg `0.4687` n `13`; crypto_alt avg `0.3852` n `235`; crypto_major avg `0.1178` n `8`; equity avg `-0.7989` n `150`; fx avg `0.0128` n `6`; index avg `-0.1505` n `26`; metal avg `-0.1668` n `20`; unknown avg `0.72` n `1031`
- 24h: commodity avg `0.8668` n `13`; crypto_alt avg `-0.7058` n `235`; crypto_major avg `-2.2281` n `8`; equity avg `-1.7428` n `150`; fx avg `-0.0073` n `6`; index avg `-0.3084` n `26`; metal avg `-0.1182` n `20`; unknown avg `416.8366` n `974`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
