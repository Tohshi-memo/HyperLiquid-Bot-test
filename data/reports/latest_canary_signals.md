# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T07:37:40.130703+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2431` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.0361` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1279` n `13`; crypto_alt avg `-0.8088` n `239`; crypto_major avg `-0.9784` n `8`; equity avg `-0.6185` n `168`; fx avg `-0.0224` n `6`; index avg `-0.0452` n `27`; metal avg `0.0292` n `20`; unknown avg `185.6325` n `1265`
- 1h: commodity avg `-0.1521` n `13`; crypto_alt avg `-1.3349` n `239`; crypto_major avg `-1.1716` n `8`; equity avg `-1.318` n `168`; fx avg `-0.0462` n `6`; index avg `-0.1355` n `27`; metal avg `-0.03` n `20`; unknown avg `1.0372` n `1257`
- 4h: commodity avg `-0.2155` n `13`; crypto_alt avg `-0.3611` n `239`; crypto_major avg `-1.4259` n `8`; equity avg `-2.0893` n `168`; fx avg `-0.1023` n `6`; index avg `-0.1828` n `27`; metal avg `-0.3072` n `20`; unknown avg `64.0715` n `1221`
- 24h: commodity avg `0.0875` n `13`; crypto_alt avg `-3.6322` n `239`; crypto_major avg `-3.915` n `8`; equity avg `-6.4012` n `167`; fx avg `0.0673` n `6`; index avg `-0.6194` n `27`; metal avg `-1.0949` n `20`; unknown avg `691.5454` n `1027`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
