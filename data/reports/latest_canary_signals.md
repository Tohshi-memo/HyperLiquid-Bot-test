# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-26T18:37:27.671469+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0878` n `12`; crypto_alt avg `-0.0382` n `230`; crypto_major avg `-0.0717` n `8`; equity avg `0.0195` n `100`; fx avg `-0.0046` n `6`; index avg `-0.0152` n `25`; metal avg `0.0043` n `20`; unknown avg `0.0049` n `775`
- 1h: commodity avg `0.1144` n `12`; crypto_alt avg `-0.1274` n `230`; crypto_major avg `-0.061` n `8`; equity avg `0.0271` n `100`; fx avg `0.0115` n `6`; index avg `-0.0216` n `25`; metal avg `0.0213` n `20`; unknown avg `-0.0527` n `775`
- 4h: commodity avg `0.0966` n `12`; crypto_alt avg `0.2103` n `230`; crypto_major avg `0.3388` n `8`; equity avg `0.1018` n `100`; fx avg `-0.0047` n `6`; index avg `0.0153` n `25`; metal avg `0.0242` n `20`; unknown avg `-0.1295` n `775`
- 24h: commodity avg `-0.3747` n `12`; crypto_alt avg `0.7041` n `230`; crypto_major avg `0.6213` n `8`; equity avg `0.719` n `100`; fx avg `0.0438` n `6`; index avg `0.1351` n `25`; metal avg `0.1902` n `20`; unknown avg `-0.0597` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1927`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.183`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1643`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1473`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1393`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1332`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1319`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1318`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1302`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1284`, n `669`, weak_sample_signal
