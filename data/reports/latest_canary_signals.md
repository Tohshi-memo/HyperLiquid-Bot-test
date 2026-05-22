# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T11:52:15.806221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2906` n `12`; crypto_alt avg `0.2764` n `228`; crypto_major avg `0.2666` n `8`; equity avg `0.1208` n `67`; fx avg `-0.0001` n `6`; index avg `0.0295` n `23`; metal avg `0.131` n `18`; unknown avg `0.0746` n `386`
- 1h: commodity avg `-0.2276` n `12`; crypto_alt avg `0.4562` n `228`; crypto_major avg `0.3912` n `8`; equity avg `0.2042` n `67`; fx avg `-0.0023` n `6`; index avg `0.1049` n `23`; metal avg `0.1055` n `18`; unknown avg `-0.0318` n `386`
- 4h: commodity avg `-0.4136` n `12`; crypto_alt avg `0.1925` n `228`; crypto_major avg `0.5059` n `8`; equity avg `-0.3805` n `67`; fx avg `-0.0091` n `6`; index avg `-0.128` n `23`; metal avg `0.3484` n `18`; unknown avg `-0.5298` n `386`
- 24h: commodity avg `-1.1302` n `12`; crypto_alt avg `2.942` n `228`; crypto_major avg `1.3122` n `8`; equity avg `1.2475` n `67`; fx avg `0.0749` n `6`; index avg `0.7643` n `23`; metal avg `0.9781` n `18`; unknown avg `1.1691` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0571`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0468`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0436`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0399`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.039`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0366`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0346`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.033`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0313`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0299`, n `668`, weak_sample_signal
