# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T01:37:26.671834+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0495` n `12`; crypto_alt avg `-0.1235` n `230`; crypto_major avg `-0.2016` n `8`; equity avg `-0.226` n `100`; fx avg `0.0138` n `6`; index avg `0.022` n `25`; metal avg `-0.0166` n `20`; unknown avg `0.2321` n `775`
- 1h: commodity avg `0.061` n `12`; crypto_alt avg `-0.1852` n `230`; crypto_major avg `-0.2444` n `8`; equity avg `-0.4909` n `100`; fx avg `0.0355` n `6`; index avg `-0.0986` n `25`; metal avg `-0.0336` n `20`; unknown avg `-0.0966` n `775`
- 4h: commodity avg `-0.2884` n `12`; crypto_alt avg `0.3605` n `230`; crypto_major avg `0.2477` n `8`; equity avg `-0.2868` n `100`; fx avg `0.0818` n `6`; index avg `-0.0384` n `25`; metal avg `0.1655` n `20`; unknown avg `-0.2924` n `775`
- 24h: commodity avg `-0.4948` n `12`; crypto_alt avg `1.2616` n `230`; crypto_major avg `1.1768` n `8`; equity avg `0.1425` n `100`; fx avg `0.1362` n `6`; index avg `0.0176` n `25`; metal avg `0.4099` n `20`; unknown avg `-0.0073` n `758`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
