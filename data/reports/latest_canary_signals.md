# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T14:52:29.429801+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0178` n `12`; crypto_alt avg `0.0742` n `233`; crypto_major avg `0.001` n `8`; equity avg `0.0001` n `136`; fx avg `-0.0059` n `6`; index avg `-0.0056` n `27`; metal avg `-0.0121` n `20`; unknown avg `0.3727` n `838`
- 1h: commodity avg `-0.1083` n `12`; crypto_alt avg `0.3094` n `233`; crypto_major avg `0.3405` n `8`; equity avg `0.1252` n `136`; fx avg `0.0033` n `6`; index avg `0.014` n `27`; metal avg `0.013` n `20`; unknown avg `3.0682` n `836`
- 4h: commodity avg `0.0566` n `12`; crypto_alt avg `1.0006` n `233`; crypto_major avg `0.7398` n `8`; equity avg `0.1852` n `136`; fx avg `0.0007` n `6`; index avg `0.034` n `27`; metal avg `0.0055` n `20`; unknown avg `3.4291` n `826`
- 24h: commodity avg `0.2036` n `12`; crypto_alt avg `0.0339` n `233`; crypto_major avg `-1.4432` n `8`; equity avg `-1.5898` n `136`; fx avg `0.0046` n `6`; index avg `-0.2562` n `26`; metal avg `-0.0758` n `20`; unknown avg `1.8363` n `708`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
