# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T04:22:25.248227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `-0.2005` n `230`; crypto_major avg `-0.2331` n `8`; equity avg `-0.0601` n `98`; fx avg `0.0047` n `6`; index avg `-0.0113` n `25`; metal avg `-0.0333` n `20`; unknown avg `-0.0331` n `771`
- 1h: commodity avg `-0.0202` n `12`; crypto_alt avg `0.0468` n `230`; crypto_major avg `0.043` n `8`; equity avg `0.4731` n `98`; fx avg `-0.0179` n `6`; index avg `0.0808` n `25`; metal avg `0.0597` n `20`; unknown avg `-0.0592` n `771`
- 4h: commodity avg `-0.0596` n `12`; crypto_alt avg `0.4789` n `230`; crypto_major avg `0.505` n `8`; equity avg `1.471` n `98`; fx avg `-0.0265` n `6`; index avg `0.3747` n `25`; metal avg `0.338` n `20`; unknown avg `0.3406` n `771`
- 24h: commodity avg `-0.3658` n `12`; crypto_alt avg `2.2931` n `230`; crypto_major avg `1.9553` n `8`; equity avg `1.1934` n `98`; fx avg `-0.1342` n `6`; index avg `0.3329` n `25`; metal avg `0.3395` n `20`; unknown avg `0.0695` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0943`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0916`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0744`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0734`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0716`, n `666`, weak_sample_signal
