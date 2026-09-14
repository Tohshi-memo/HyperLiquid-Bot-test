# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T05:52:27.905127+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0307` n `12`; crypto_alt avg `-0.1063` n `233`; crypto_major avg `-0.1087` n `8`; equity avg `-0.0851` n `136`; fx avg `0.0095` n `6`; index avg `-0.0166` n `27`; metal avg `-0.0578` n `20`; unknown avg `3.1479` n `894`
- 1h: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.1567` n `233`; crypto_major avg `-0.1583` n `8`; equity avg `-0.2124` n `136`; fx avg `0.0315` n `6`; index avg `-0.0194` n `27`; metal avg `-0.0108` n `20`; unknown avg `7.3459` n `892`
- 4h: commodity avg `-0.0206` n `12`; crypto_alt avg `0.9736` n `233`; crypto_major avg `1.2692` n `8`; equity avg `-0.0541` n `136`; fx avg `-0.0031` n `6`; index avg `-0.0209` n `27`; metal avg `-0.1064` n `20`; unknown avg `10.6643` n `880`
- 24h: commodity avg `0.5463` n `12`; crypto_alt avg `-0.7745` n `233`; crypto_major avg `-0.1983` n `8`; equity avg `-1.5012` n `136`; fx avg `0.0542` n `6`; index avg `-0.3305` n `26`; metal avg `-0.1881` n `20`; unknown avg `1.4547` n `676`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
