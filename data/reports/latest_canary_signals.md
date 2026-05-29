# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T05:07:17.606816+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.011` n `12`; crypto_alt avg `0.3801` n `228`; crypto_major avg `0.3008` n `8`; equity avg `0.0852` n `69`; fx avg `0.0026` n `6`; index avg `0.0743` n `23`; metal avg `0.0429` n `18`; unknown avg `-0.0988` n `417`
- 1h: commodity avg `-0.0865` n `12`; crypto_alt avg `0.7066` n `228`; crypto_major avg `0.4737` n `8`; equity avg `0.3373` n `69`; fx avg `0.016` n `6`; index avg `0.1413` n `23`; metal avg `0.2199` n `18`; unknown avg `-0.0595` n `417`
- 4h: commodity avg `-0.0925` n `12`; crypto_alt avg `-0.5332` n `228`; crypto_major avg `-0.3381` n `8`; equity avg `0.4644` n `69`; fx avg `-0.0107` n `6`; index avg `0.2263` n `23`; metal avg `0.0307` n `18`; unknown avg `-0.7508` n `417`
- 24h: commodity avg `-0.2421` n `12`; crypto_alt avg `1.1422` n `228`; crypto_major avg `1.8941` n `8`; equity avg `4.9274` n `69`; fx avg `0.1673` n `6`; index avg `1.8034` n `23`; metal avg `2.7936` n `18`; unknown avg `0.733` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
