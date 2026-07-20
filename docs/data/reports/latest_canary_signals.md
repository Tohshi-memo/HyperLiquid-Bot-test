# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T05:52:26.991948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0031` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0297` n `12`; crypto_alt avg `-0.103` n `230`; crypto_major avg `-0.088` n `8`; equity avg `-0.1011` n `98`; fx avg `-0.0027` n `6`; index avg `-0.0165` n `25`; metal avg `-0.0406` n `20`; unknown avg `8.3267` n `769`
- 1h: commodity avg `0.0213` n `12`; crypto_alt avg `-0.6682` n `230`; crypto_major avg `-0.6249` n `8`; equity avg `-0.5365` n `98`; fx avg `-0.0013` n `6`; index avg `-0.1426` n `25`; metal avg `-0.1783` n `20`; unknown avg `3.489` n `769`
- 4h: commodity avg `0.0172` n `12`; crypto_alt avg `-1.1991` n `230`; crypto_major avg `-1.0748` n `8`; equity avg `-0.2229` n `98`; fx avg `-0.0184` n `6`; index avg `-0.0717` n `25`; metal avg `-0.0284` n `20`; unknown avg `0.7349` n `769`
- 24h: commodity avg `-0.013` n `12`; crypto_alt avg `-0.8812` n `230`; crypto_major avg `-0.7115` n `8`; equity avg `-0.0853` n `97`; fx avg `-0.0313` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0852` n `20`; unknown avg `-0.1253` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1088`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1021`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0966`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0899`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0877`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0831`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
