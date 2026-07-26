# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T05:07:27.358175+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.1079` n `230`; crypto_major avg `-0.023` n `8`; equity avg `-0.0372` n `100`; fx avg `0.0028` n `6`; index avg `0.0001` n `25`; metal avg `0.0003` n `20`; unknown avg `0.0504` n `775`
- 1h: commodity avg `-0.0482` n `12`; crypto_alt avg `0.0313` n `230`; crypto_major avg `0.1403` n `8`; equity avg `-0.0096` n `100`; fx avg `0.029` n `6`; index avg `-0.0004` n `25`; metal avg `0.0089` n `20`; unknown avg `-0.1094` n `775`
- 4h: commodity avg `-0.0551` n `12`; crypto_alt avg `0.4505` n `230`; crypto_major avg `0.4726` n `8`; equity avg `0.1835` n `100`; fx avg `0.0725` n `6`; index avg `0.0379` n `25`; metal avg `0.0261` n `20`; unknown avg `-0.0904` n `774`
- 24h: commodity avg `-0.5411` n `12`; crypto_alt avg `0.793` n `230`; crypto_major avg `1.4459` n `8`; equity avg `0.4672` n `100`; fx avg `0.0698` n `6`; index avg `0.1257` n `25`; metal avg `0.059` n `20`; unknown avg `-0.1587` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1832`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.138`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1238`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1211`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1187`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1177`, n `666`, weak_sample_signal
