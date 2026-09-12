# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T02:07:29.470294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.98` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0054` n `12`; crypto_alt avg `0.0253` n `233`; crypto_major avg `0.0272` n `8`; equity avg `-0.0178` n `136`; fx avg `-0.0016` n `6`; index avg `0.0005` n `26`; metal avg `0.0007` n `20`; unknown avg `4.2577` n `836`
- 1h: commodity avg `-0.0668` n `12`; crypto_alt avg `0.1588` n `233`; crypto_major avg `0.0788` n `8`; equity avg `0.0081` n `136`; fx avg `0.0005` n `6`; index avg `-0.0138` n `26`; metal avg `-0.023` n `20`; unknown avg `0.3509` n `832`
- 4h: commodity avg `-0.0988` n `12`; crypto_alt avg `1.0463` n `233`; crypto_major avg `0.1199` n `8`; equity avg `0.1269` n `136`; fx avg `0.0053` n `6`; index avg `0.0147` n `26`; metal avg `-0.0404` n `20`; unknown avg `2.0365` n `820`
- 24h: commodity avg `-0.7122` n `12`; crypto_alt avg `1.462` n `233`; crypto_major avg `1.3615` n `8`; equity avg `0.8808` n `136`; fx avg `-0.1644` n `6`; index avg `0.3042` n `26`; metal avg `0.2422` n `20`; unknown avg `29.7376` n `700`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
