# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T14:22:29.933276+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7552` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.4514` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9689` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_metal_divergence: score `1.7061` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.208` n `13`; crypto_alt avg `0.3675` n `237`; crypto_major avg `0.1572` n `8`; equity avg `0.3612` n `151`; fx avg `0.0046` n `6`; index avg `0.0612` n `26`; metal avg `0.1203` n `20`; unknown avg `2.016` n `1196`
- 1h: commodity avg `-0.5299` n `13`; crypto_alt avg `2.3987` n `237`; crypto_major avg `1.9215` n `8`; equity avg `1.5552` n `151`; fx avg `0.0387` n `6`; index avg `0.2383` n `26`; metal avg `0.2154` n `20`; unknown avg `43.5489` n `1106`
- 4h: commodity avg `-0.5862` n `13`; crypto_alt avg `2.7696` n `237`; crypto_major avg `2.169` n `8`; equity avg `1.4639` n `151`; fx avg `0.0757` n `6`; index avg `0.2372` n `26`; metal avg `0.2001` n `20`; unknown avg `2.8355` n `1100`
- 24h: commodity avg `-0.1785` n `13`; crypto_alt avg `3.0173` n `237`; crypto_major avg `2.0289` n `8`; equity avg `-0.4915` n `151`; fx avg `0.0568` n `6`; index avg `-0.0902` n `26`; metal avg `0.1034` n `20`; unknown avg `3.9043` n `1043`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
