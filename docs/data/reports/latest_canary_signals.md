# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T07:07:48.616905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0076` n `13`; crypto_alt avg `-0.1604` n `235`; crypto_major avg `-0.1067` n `8`; equity avg `0.0492` n `150`; fx avg `0.0071` n `6`; index avg `0.0028` n `26`; metal avg `0.0289` n `20`; unknown avg `-0.0355` n `1076`
- 1h: commodity avg `0.0509` n `13`; crypto_alt avg `0.0386` n `235`; crypto_major avg `0.0056` n `8`; equity avg `0.1188` n `150`; fx avg `-0.0014` n `6`; index avg `0.02` n `26`; metal avg `0.0172` n `20`; unknown avg `0.68` n `1076`
- 4h: commodity avg `0.0243` n `13`; crypto_alt avg `0.9394` n `235`; crypto_major avg `0.4111` n `8`; equity avg `0.8234` n `150`; fx avg `0.0183` n `6`; index avg `0.0872` n `26`; metal avg `0.1628` n `20`; unknown avg `2.314` n `1040`
- 24h: commodity avg `-0.1291` n `13`; crypto_alt avg `-1.0186` n `235`; crypto_major avg `-2.0028` n `8`; equity avg `-0.4547` n `150`; fx avg `0.1445` n `6`; index avg `0.0495` n `26`; metal avg `0.4559` n `20`; unknown avg `6.5243` n `989`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
