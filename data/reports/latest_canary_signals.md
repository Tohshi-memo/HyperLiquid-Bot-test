# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T04:22:24.041373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `-0.2483` n `230`; crypto_major avg `-0.249` n `8`; equity avg `-0.104` n `98`; fx avg `-0.0032` n `6`; index avg `-0.0275` n `25`; metal avg `-0.0187` n `20`; unknown avg `-0.1101` n `769`
- 1h: commodity avg `0.0359` n `12`; crypto_alt avg `-0.4325` n `230`; crypto_major avg `-0.3743` n `8`; equity avg `-0.0083` n `98`; fx avg `-0.0051` n `6`; index avg `-0.0336` n `25`; metal avg `-0.1` n `20`; unknown avg `-0.1381` n `769`
- 4h: commodity avg `0.0066` n `12`; crypto_alt avg `-0.7024` n `230`; crypto_major avg `-0.5724` n `8`; equity avg `-0.7857` n `98`; fx avg `-0.0522` n `6`; index avg `-0.1914` n `25`; metal avg `0.0815` n `20`; unknown avg `-0.1409` n `769`
- 24h: commodity avg `-0.0314` n `12`; crypto_alt avg `-0.2209` n `230`; crypto_major avg `-0.0661` n `8`; equity avg `0.1599` n `97`; fx avg `-0.0213` n `6`; index avg `-0.0012` n `25`; metal avg `0.0852` n `20`; unknown avg `-0.0057` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1023`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0981`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0908`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0875`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.084`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0787`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
