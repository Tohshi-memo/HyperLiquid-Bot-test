# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T13:07:30.837288+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1956` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0803` n `12`; crypto_alt avg `-0.8071` n `230`; crypto_major avg `-0.6713` n `8`; equity avg `-0.2162` n `100`; fx avg `0.0003` n `6`; index avg `-0.0497` n `25`; metal avg `-0.1335` n `20`; unknown avg `-0.1635` n `773`
- 1h: commodity avg `0.0856` n `12`; crypto_alt avg `-1.077` n `230`; crypto_major avg `-0.8774` n `8`; equity avg `-0.2768` n `100`; fx avg `-0.0033` n `6`; index avg `-0.0761` n `25`; metal avg `-0.1668` n `20`; unknown avg `-0.1301` n `773`
- 4h: commodity avg `0.2825` n `12`; crypto_alt avg `-1.4799` n `230`; crypto_major avg `-1.2455` n `8`; equity avg `-0.2344` n `100`; fx avg `-0.0345` n `6`; index avg `-0.0499` n `25`; metal avg `-0.1085` n `20`; unknown avg `-0.1026` n `773`
- 24h: commodity avg `-0.1942` n `12`; crypto_alt avg `-1.9955` n `230`; crypto_major avg `-2.0384` n `8`; equity avg `-0.611` n `100`; fx avg `-0.1715` n `6`; index avg `-0.2158` n `25`; metal avg `-0.0692` n `20`; unknown avg `0.0753` n `756`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0989`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0864`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
