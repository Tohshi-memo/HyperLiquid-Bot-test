# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T11:52:32.129219+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2615` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.6874` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.577` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.023` n `12`; crypto_alt avg `-0.1353` n `234`; crypto_major avg `-0.0261` n `8`; equity avg `0.0392` n `141`; fx avg `-0.0208` n `6`; index avg `-0.0085` n `26`; metal avg `0.0114` n `20`; unknown avg `5.9401` n `944`
- 1h: commodity avg `-0.1585` n `12`; crypto_alt avg `0.6307` n `234`; crypto_major avg `0.5813` n `8`; equity avg `0.0972` n `141`; fx avg `-0.0152` n `6`; index avg `0.0371` n `26`; metal avg `-0.0676` n `20`; unknown avg `4.7141` n `942`
- 4h: commodity avg `-0.309` n `12`; crypto_alt avg `2.2091` n `234`; crypto_major avg `1.9525` n `8`; equity avg `0.3755` n `141`; fx avg `-0.0476` n `6`; index avg `0.0696` n `26`; metal avg `0.2651` n `20`; unknown avg `2.4564` n `924`
- 24h: commodity avg `-0.0685` n `12`; crypto_alt avg `5.9209` n `234`; crypto_major avg `3.8451` n `8`; equity avg `1.988` n `141`; fx avg `-0.2372` n `6`; index avg `0.3259` n `26`; metal avg `0.2417` n `20`; unknown avg `13.4474` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
