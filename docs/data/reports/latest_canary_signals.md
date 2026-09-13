# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T18:52:29.274475+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `0.1181` n `233`; crypto_major avg `0.059` n `8`; equity avg `-0.005` n `136`; fx avg `-0.0011` n `6`; index avg `-0.0047` n `27`; metal avg `0.0076` n `20`; unknown avg `-0.4308` n `832`
- 1h: commodity avg `-0.0057` n `12`; crypto_alt avg `0.1053` n `233`; crypto_major avg `0.0789` n `8`; equity avg `0.0234` n `136`; fx avg `0.0037` n `6`; index avg `0.0035` n `27`; metal avg `0.0063` n `20`; unknown avg `-0.4105` n `830`
- 4h: commodity avg `0.1051` n `12`; crypto_alt avg `0.1474` n `233`; crypto_major avg `0.4542` n `8`; equity avg `0.2242` n `136`; fx avg `0.0058` n `6`; index avg `-0.0118` n `27`; metal avg `0.0195` n `20`; unknown avg `1.7478` n `766`
- 24h: commodity avg `0.2405` n `12`; crypto_alt avg `0.2525` n `233`; crypto_major avg `-0.549` n `8`; equity avg `-1.3538` n `136`; fx avg `0.0152` n `6`; index avg `-0.2645` n `26`; metal avg `-0.0689` n `20`; unknown avg `1.3228` n `720`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0658`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
