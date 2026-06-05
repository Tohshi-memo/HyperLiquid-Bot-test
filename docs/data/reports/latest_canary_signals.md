# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T15:22:25.302343+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.1723` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.5536` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.07` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.022` n `12`; crypto_alt avg `-0.9152` n `228`; crypto_major avg `-0.6042` n `8`; equity avg `-0.5135` n `74`; fx avg `-0.0014` n `6`; index avg `0.0274` n `23`; metal avg `-0.6063` n `18`; unknown avg `-0.4608` n `424`
- 1h: commodity avg `-0.1644` n `12`; crypto_alt avg `-1.4138` n `228`; crypto_major avg `-1.1136` n `8`; equity avg `-0.8791` n `74`; fx avg `-0.0428` n `6`; index avg `-0.0436` n `23`; metal avg `-0.665` n `18`; unknown avg `-0.739` n `424`
- 4h: commodity avg `-0.8712` n `12`; crypto_alt avg `-2.6929` n `228`; crypto_major avg `-3.0435` n `8`; equity avg `-3.1626` n `74`; fx avg `-0.1391` n `6`; index avg `-1.4899` n `23`; metal avg `-3.076` n `18`; unknown avg `0.4543` n `424`
- 24h: commodity avg `-0.9181` n `12`; crypto_alt avg `-8.4393` n `228`; crypto_major avg `-6.3849` n `8`; equity avg `-4.8476` n `74`; fx avg `0.0016` n `6`; index avg `-2.0853` n `23`; metal avg `-3.6783` n `18`; unknown avg `-0.9329` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
