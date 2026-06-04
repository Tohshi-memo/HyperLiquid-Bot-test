# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T17:52:27.095087+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1199` n `12`; crypto_alt avg `0.4554` n `228`; crypto_major avg `0.6189` n `8`; equity avg `0.1016` n `74`; fx avg `0.0007` n `6`; index avg `0.0683` n `23`; metal avg `-0.0569` n `18`; unknown avg `0.2347` n `424`
- 1h: commodity avg `0.0373` n `12`; crypto_alt avg `-0.2863` n `228`; crypto_major avg `-0.3423` n `8`; equity avg `0.1754` n `74`; fx avg `-0.0099` n `6`; index avg `0.1898` n `23`; metal avg `0.0092` n `18`; unknown avg `2.3561` n `424`
- 4h: commodity avg `-0.1952` n `12`; crypto_alt avg `0.5591` n `228`; crypto_major avg `0.0508` n `8`; equity avg `0.8059` n `74`; fx avg `-0.0372` n `6`; index avg `0.7718` n `23`; metal avg `-0.3861` n `18`; unknown avg `2.6016` n `424`
- 24h: commodity avg `-0.8895` n `12`; crypto_alt avg `-5.2057` n `228`; crypto_major avg `-3.8815` n `8`; equity avg `-1.063` n `73`; fx avg `0.066` n `6`; index avg `0.0149` n `23`; metal avg `0.6784` n `18`; unknown avg `0.256` n `401`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
