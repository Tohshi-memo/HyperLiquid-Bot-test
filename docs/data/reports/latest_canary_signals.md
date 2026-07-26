# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T07:22:28.539378+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0486` n `12`; crypto_alt avg `-0.0241` n `230`; crypto_major avg `-0.0687` n `8`; equity avg `-0.034` n `100`; fx avg `-0.0107` n `6`; index avg `-0.0041` n `25`; metal avg `0.0067` n `20`; unknown avg `-0.0307` n `775`
- 1h: commodity avg `-0.1336` n `12`; crypto_alt avg `0.442` n `230`; crypto_major avg `0.3228` n `8`; equity avg `0.0647` n `100`; fx avg `-0.0082` n `6`; index avg `0.0045` n `25`; metal avg `0.0117` n `20`; unknown avg `0.0283` n `775`
- 4h: commodity avg `-0.0661` n `12`; crypto_alt avg `0.4871` n `230`; crypto_major avg `0.2338` n `8`; equity avg `0.0361` n `100`; fx avg `0.0489` n `6`; index avg `0.0023` n `25`; metal avg `0.0209` n `20`; unknown avg `-0.0046` n `759`
- 24h: commodity avg `-0.5922` n `12`; crypto_alt avg `1.6596` n `230`; crypto_major avg `1.7802` n `8`; equity avg `0.5281` n `100`; fx avg `0.0131` n `6`; index avg `0.1329` n `25`; metal avg `0.0526` n `20`; unknown avg `-0.1178` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.172`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1399`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1246`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1221`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1212`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1179`, n `666`, weak_sample_signal
