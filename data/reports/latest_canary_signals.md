# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T10:07:28.584717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0775` n `12`; crypto_alt avg `-0.1519` n `233`; crypto_major avg `-0.1098` n `8`; equity avg `0.0382` n `136`; fx avg `-0.0287` n `6`; index avg `-0.002` n `27`; metal avg `0.0522` n `20`; unknown avg `0.2989` n `906`
- 1h: commodity avg `-0.0371` n `12`; crypto_alt avg `0.0393` n `233`; crypto_major avg `0.1737` n `8`; equity avg `0.3441` n `136`; fx avg `-0.0308` n `6`; index avg `0.0718` n `27`; metal avg `0.1095` n `20`; unknown avg `-0.3312` n `906`
- 4h: commodity avg `0.0259` n `12`; crypto_alt avg `-0.6662` n `233`; crypto_major avg `-0.6843` n `8`; equity avg `-0.0304` n `136`; fx avg `0.03` n `6`; index avg `-0.0214` n `27`; metal avg `-0.059` n `20`; unknown avg `0.4779` n `898`
- 24h: commodity avg `0.0519` n `12`; crypto_alt avg `-1.556` n `233`; crypto_major avg `-1.1381` n `8`; equity avg `0.2367` n `136`; fx avg `0.202` n `6`; index avg `0.0338` n `27`; metal avg `0.0409` n `20`; unknown avg `-0.7679` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0809`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
