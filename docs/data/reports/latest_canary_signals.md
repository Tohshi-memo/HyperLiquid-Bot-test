# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T20:37:20.639076+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.04` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.242` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0271` n `12`; crypto_alt avg `-0.1782` n `228`; crypto_major avg `-0.1933` n `8`; equity avg `0.0529` n `69`; fx avg `0.0039` n `6`; index avg `0.0526` n `23`; metal avg `0.0061` n `18`; unknown avg `-0.0406` n `422`
- 1h: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.2049` n `228`; crypto_major avg `-0.0372` n `8`; equity avg `-0.1011` n `69`; fx avg `0.0001` n `6`; index avg `-0.1379` n `23`; metal avg `-0.098` n `18`; unknown avg `-0.1776` n `422`
- 4h: commodity avg `-0.8916` n `12`; crypto_alt avg `1.278` n `228`; crypto_major avg `1.3504` n `8`; equity avg `0.1318` n `69`; fx avg `0.0383` n `6`; index avg `0.2968` n `23`; metal avg `0.1816` n `18`; unknown avg `0.5451` n `422`
- 24h: commodity avg `0.4568` n `12`; crypto_alt avg `1.3281` n `228`; crypto_major avg `-0.2603` n `8`; equity avg `-0.053` n `69`; fx avg `0.057` n `6`; index avg `0.3552` n `23`; metal avg `-0.0369` n `18`; unknown avg `2.8887` n `405`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.184`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
