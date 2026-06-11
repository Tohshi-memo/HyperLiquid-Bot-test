# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T02:07:23.841218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1228` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `-0.1408` n `228`; crypto_major avg `-0.2393` n `8`; equity avg `-0.1882` n `74`; fx avg `0.0034` n `6`; index avg `-0.0686` n `23`; metal avg `-0.1626` n `18`; unknown avg `-0.0307` n `550`
- 1h: commodity avg `-0.2672` n `12`; crypto_alt avg `0.4643` n `228`; crypto_major avg `0.6795` n `8`; equity avg `-0.0743` n `74`; fx avg `0.0513` n `6`; index avg `0.0786` n `23`; metal avg `0.6175` n `18`; unknown avg `0.2151` n `550`
- 4h: commodity avg `-0.1622` n `12`; crypto_alt avg `2.7551` n `228`; crypto_major avg `1.9606` n `8`; equity avg `1.0614` n `74`; fx avg `0.1701` n `6`; index avg `0.5467` n `23`; metal avg `1.1422` n `18`; unknown avg `1.1569` n `550`
- 24h: commodity avg `1.2295` n `12`; crypto_alt avg `-0.6` n `228`; crypto_major avg `-0.6793` n `8`; equity avg `-1.1586` n `74`; fx avg `0.1055` n `6`; index avg `-1.144` n `23`; metal avg `-0.4902` n `18`; unknown avg `0.071` n `537`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2228`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1898`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
