# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T15:22:27.518566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1464` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9823` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0713` n `12`; crypto_alt avg `-0.2627` n `228`; crypto_major avg `-0.8629` n `8`; equity avg `0.1413` n `74`; fx avg `-0.0166` n `6`; index avg `0.1109` n `23`; metal avg `0.0769` n `18`; unknown avg `-0.2833` n `424`
- 1h: commodity avg `0.0924` n `12`; crypto_alt avg `0.4621` n `228`; crypto_major avg `-0.1819` n `8`; equity avg `0.7608` n `74`; fx avg `-0.0268` n `6`; index avg `0.4547` n `23`; metal avg `-0.0677` n `18`; unknown avg `-0.2168` n `424`
- 4h: commodity avg `-0.1415` n `12`; crypto_alt avg `3.0811` n `228`; crypto_major avg `2.0049` n `8`; equity avg `1.8184` n `73`; fx avg `-0.023` n `6`; index avg `0.7113` n `23`; metal avg `0.0226` n `18`; unknown avg `1.2287` n `422`
- 24h: commodity avg `-0.4542` n `12`; crypto_alt avg `-5.8672` n `228`; crypto_major avg `-4.2934` n `8`; equity avg `-1.438` n `73`; fx avg `0.0907` n `6`; index avg `-0.3847` n `23`; metal avg `0.2067` n `18`; unknown avg `-1.3941` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1519`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1326`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
