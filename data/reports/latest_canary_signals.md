# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T14:07:29.775758+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1041` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0697` n `12`; crypto_alt avg `0.2928` n `228`; crypto_major avg `0.5048` n `8`; equity avg `-0.0795` n `73`; fx avg `-0.0015` n `6`; index avg `-0.2829` n `23`; metal avg `-0.3208` n `18`; unknown avg `1.0818` n `425`
- 1h: commodity avg `0.0698` n `12`; crypto_alt avg `0.5039` n `228`; crypto_major avg `0.5166` n `8`; equity avg `0.421` n `73`; fx avg `-0.0206` n `6`; index avg `-0.1323` n `23`; metal avg `-0.4339` n `18`; unknown avg `0.1919` n `425`
- 4h: commodity avg `-0.2323` n `12`; crypto_alt avg `2.2153` n `228`; crypto_major avg `1.8718` n `8`; equity avg `0.6631` n `73`; fx avg `-0.007` n `6`; index avg `-0.1743` n `23`; metal avg `0.399` n `18`; unknown avg `1.7577` n `422`
- 24h: commodity avg `-0.2111` n `12`; crypto_alt avg `-6.138` n `228`; crypto_major avg `-4.1404` n `8`; equity avg `-2.232` n `73`; fx avg `0.1076` n `6`; index avg `-1.0976` n `23`; metal avg `0.1782` n `18`; unknown avg `-0.229` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
