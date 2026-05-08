# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T20:22:19.947639+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0009` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0231` n `12`; crypto_alt avg `0.1119` n `228`; crypto_major avg `0.1182` n `8`; equity avg `0.0243` n `65`; fx avg `0.0102` n `5`; index avg `-0.0404` n `23`; metal avg `-0.1244` n `18`; unknown avg `-0.0339` n `375`
- 1h: commodity avg `-0.152` n `12`; crypto_alt avg `-0.1122` n `228`; crypto_major avg `-0.1225` n `8`; equity avg `0.4314` n `65`; fx avg `0.0199` n `5`; index avg `0.032` n `23`; metal avg `-0.1143` n `18`; unknown avg `-0.2066` n `375`
- 4h: commodity avg `-0.9086` n `12`; crypto_alt avg `1.1334` n `228`; crypto_major avg `1.0923` n `8`; equity avg `1.0667` n `65`; fx avg `0.0439` n `5`; index avg `0.355` n `23`; metal avg `0.1375` n `18`; unknown avg `-0.1328` n `375`
- 24h: commodity avg `-0.0848` n `12`; crypto_alt avg `2.8738` n `228`; crypto_major avg `1.3351` n `8`; equity avg `3.5035` n `65`; fx avg `0.2103` n `5`; index avg `1.4696` n `23`; metal avg `0.4035` n `18`; unknown avg `0.6293` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
