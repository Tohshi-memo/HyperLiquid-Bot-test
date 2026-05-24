# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T04:07:17.020637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0573` n `12`; crypto_alt avg `0.0784` n `228`; crypto_major avg `0.0325` n `8`; equity avg `-0.0707` n `67`; fx avg `-0.0024` n `6`; index avg `0.0042` n `23`; metal avg `0.0148` n `18`; unknown avg `-0.2903` n `396`
- 1h: commodity avg `-0.3279` n `12`; crypto_alt avg `-0.4123` n `228`; crypto_major avg `-0.1455` n `8`; equity avg `-0.1355` n `67`; fx avg `0.0001` n `6`; index avg `-0.031` n `23`; metal avg `0.0935` n `18`; unknown avg `-0.4505` n `396`
- 4h: commodity avg `0.1184` n `12`; crypto_alt avg `-0.3613` n `228`; crypto_major avg `0.4177` n `8`; equity avg `0.1068` n `67`; fx avg `-0.0178` n `6`; index avg `0.2104` n `23`; metal avg `0.2787` n `18`; unknown avg `-0.527` n `396`
- 24h: commodity avg `-3.0301` n `12`; crypto_alt avg `1.4912` n `228`; crypto_major avg `2.1234` n `8`; equity avg `2.0302` n `67`; fx avg `0.0347` n `6`; index avg `1.1325` n `23`; metal avg `1.2227` n `18`; unknown avg `1.4206` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0815`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
