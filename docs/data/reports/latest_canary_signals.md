# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T15:37:23.174409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0327` n `13`; crypto_alt avg `-0.3492` n `236`; crypto_major avg `-0.2393` n `8`; equity avg `-0.0944` n `151`; fx avg `-0.0251` n `6`; index avg `-0.0128` n `26`; metal avg `-0.0036` n `20`; unknown avg `0.0431` n `1193`
- 1h: commodity avg `0.0914` n `13`; crypto_alt avg `-0.6124` n `236`; crypto_major avg `-0.4301` n `8`; equity avg `-0.222` n `151`; fx avg `-0.0167` n `6`; index avg `-0.0299` n `26`; metal avg `-0.0107` n `20`; unknown avg `2.4662` n `1175`
- 4h: commodity avg `0.1452` n `13`; crypto_alt avg `-1.2398` n `236`; crypto_major avg `-0.6425` n `8`; equity avg `-0.3496` n `151`; fx avg `-0.0225` n `6`; index avg `-0.0697` n `26`; metal avg `-0.0289` n `20`; unknown avg `5.4898` n `1167`
- 24h: commodity avg `0.7617` n `13`; crypto_alt avg `-2.535` n `236`; crypto_major avg `-0.9582` n `8`; equity avg `-1.7368` n `151`; fx avg `-0.0268` n `6`; index avg `-0.3401` n `26`; metal avg `-0.1608` n `20`; unknown avg `1.0455` n `1030`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.172`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1453`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1155`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1123`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.071`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
