# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T14:07:45.009287+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0103` n `12`; crypto_alt avg `-0.0217` n `233`; crypto_major avg `0.0509` n `8`; equity avg `0.297` n `136`; fx avg `-0.009` n `6`; index avg `0.0105` n `27`; metal avg `-0.0542` n `20`; unknown avg `0.0413` n `892`
- 1h: commodity avg `-0.0017` n `12`; crypto_alt avg `0.7198` n `233`; crypto_major avg `0.855` n `8`; equity avg `1.0034` n `136`; fx avg `0.0072` n `6`; index avg `0.1283` n `27`; metal avg `-0.0193` n `20`; unknown avg `2.0927` n `878`
- 4h: commodity avg `0.1835` n `12`; crypto_alt avg `-0.5782` n `233`; crypto_major avg `-0.1924` n `8`; equity avg `0.4233` n `136`; fx avg `0.0467` n `6`; index avg `0.0636` n `27`; metal avg `-0.0176` n `20`; unknown avg `0.5357` n `872`
- 24h: commodity avg `0.6272` n `12`; crypto_alt avg `-0.7724` n `233`; crypto_major avg `1.608` n `8`; equity avg `-0.5672` n `136`; fx avg `0.0759` n `6`; index avg `-0.2255` n `27`; metal avg `-0.532` n `20`; unknown avg `1.2572` n `636`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.109`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
