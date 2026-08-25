# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T14:22:35.693446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0292` n `12`; crypto_alt avg `-0.0403` n `231`; crypto_major avg `0.1115` n `8`; equity avg `-0.298` n `122`; fx avg `-0.0028` n `6`; index avg `-0.0319` n `25`; metal avg `0.0204` n `20`; unknown avg `-0.0752` n `795`
- 1h: commodity avg `0.0354` n `12`; crypto_alt avg `0.2787` n `231`; crypto_major avg `0.5264` n `8`; equity avg `-0.1848` n `122`; fx avg `-0.0014` n `6`; index avg `-0.0802` n `25`; metal avg `0.1389` n `20`; unknown avg `-0.0014` n `795`
- 4h: commodity avg `-0.0523` n `12`; crypto_alt avg `-0.9275` n `231`; crypto_major avg `-0.7449` n `8`; equity avg `-0.4191` n `122`; fx avg `0.0184` n `6`; index avg `-0.1132` n `25`; metal avg `-0.0301` n `20`; unknown avg `-0.1402` n `795`
- 24h: commodity avg `-0.7548` n `12`; crypto_alt avg `-1.5246` n `231`; crypto_major avg `-0.8882` n `8`; equity avg `1.6329` n `122`; fx avg `0.0294` n `6`; index avg `0.2265` n `25`; metal avg `-0.434` n `20`; unknown avg `-1.0258` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0672`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
