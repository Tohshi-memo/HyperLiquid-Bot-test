# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T21:37:30.691113+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.5076` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.3996` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0364` n `13`; crypto_alt avg `-0.0933` n `235`; crypto_major avg `-0.0461` n `8`; equity avg `-0.0185` n `143`; fx avg `-0.0622` n `6`; index avg `0.0018` n `26`; metal avg `0.0044` n `20`; unknown avg `-0.0698` n `984`
- 1h: commodity avg `0.0889` n `13`; crypto_alt avg `-0.221` n `235`; crypto_major avg `-0.0691` n `8`; equity avg `-0.0302` n `143`; fx avg `0.0011` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0004` n `20`; unknown avg `1.4656` n `980`
- 4h: commodity avg `0.319` n `13`; crypto_alt avg `-2.5096` n `235`; crypto_major avg `-1.3588` n `8`; equity avg `0.1488` n `143`; fx avg `-0.024` n `6`; index avg `0.0408` n `26`; metal avg `0.1237` n `20`; unknown avg `8.4065` n `922`
- 24h: commodity avg `0.0044` n `13`; crypto_alt avg `-1.2866` n `235`; crypto_major avg `-0.6735` n `8`; equity avg `0.7848` n `142`; fx avg `-0.1645` n `6`; index avg `0.3054` n `26`; metal avg `-0.246` n `20`; unknown avg `0.0905` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
