# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T03:07:23.588026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.3971` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.6191` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_crypto_metal_divergence: score `-1.5838` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_index_leads_crypto: score `1.5733` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0602` n `12`; crypto_alt avg `-0.7568` n `228`; crypto_major avg `-0.6345` n `8`; equity avg `-0.2137` n `74`; fx avg `0.0163` n `6`; index avg `-0.0368` n `23`; metal avg `-0.2979` n `18`; unknown avg `-0.3754` n `424`
- 1h: commodity avg `0.0682` n `12`; crypto_alt avg `-2.2962` n `228`; crypto_major avg `-1.6615` n `8`; equity avg `-0.2831` n `74`; fx avg `-0.0228` n `6`; index avg `-0.0882` n `23`; metal avg `-0.0777` n `18`; unknown avg `-0.2426` n `424`
- 4h: commodity avg `0.1376` n `12`; crypto_alt avg `-2.9483` n `228`; crypto_major avg `-2.2595` n `8`; equity avg `-0.84` n `74`; fx avg `0.1305` n `6`; index avg `-0.6404` n `23`; metal avg `-1.0226` n `18`; unknown avg `0.2666` n `424`
- 24h: commodity avg `0.0224` n `12`; crypto_alt avg `-6.4072` n `228`; crypto_major avg `-4.8906` n `8`; equity avg `-1.4246` n `73`; fx avg `0.2091` n `6`; index avg `-0.4446` n `23`; metal avg `-0.8691` n `18`; unknown avg `-1.3433` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
