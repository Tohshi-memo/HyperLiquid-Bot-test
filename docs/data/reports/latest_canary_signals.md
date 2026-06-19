# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-19T19:37:30.998615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-5.3804` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `-5.0305` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `4.9594` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0047` n `12`; crypto_alt avg `-0.1798` n `228`; crypto_major avg `-0.168` n `8`; equity avg `-0.0387` n `78`; fx avg `-0.037` n `6`; index avg `-0.0025` n `23`; metal avg `0.0141` n `18`; unknown avg `-0.1187` n `687`
- 1h: commodity avg `0.0033` n `12`; crypto_alt avg `-0.4541` n `228`; crypto_major avg `-0.1535` n `8`; equity avg `-0.0451` n `78`; fx avg `-0.0641` n `6`; index avg `0.0077` n `23`; metal avg `0.0262` n `18`; unknown avg `-0.1602` n `687`
- 4h: commodity avg `0.3006` n `12`; crypto_alt avg `-4.0315` n `228`; crypto_major avg `-4.7299` n `8`; equity avg `0.6505` n `78`; fx avg `-0.1351` n `6`; index avg `0.2295` n `23`; metal avg `-4.2188` n `18`; unknown avg `-0.4381` n `572`
- 24h: commodity avg `0.3006` n `12`; crypto_alt avg `-4.0315` n `228`; crypto_major avg `-4.7299` n `8`; equity avg `0.6505` n `78`; fx avg `-0.1351` n `6`; index avg `0.2295` n `23`; metal avg `-4.2188` n `18`; unknown avg `-0.4381` n `572`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0552`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
