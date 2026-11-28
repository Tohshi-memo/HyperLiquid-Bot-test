# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T06:07:30.037240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.087` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0004` n `13`; crypto_alt avg `-0.0737` n `239`; crypto_major avg `-0.0283` n `8`; equity avg `-0.0562` n `168`; fx avg `0.0099` n `6`; index avg `-0.0065` n `27`; metal avg `-0.0076` n `20`; unknown avg `9.0918` n `1233`
- 1h: commodity avg `-0.0026` n `13`; crypto_alt avg `-0.7824` n `239`; crypto_major avg `-0.2151` n `8`; equity avg `-0.2075` n `168`; fx avg `0.0003` n `6`; index avg `-0.019` n `27`; metal avg `-0.0215` n `20`; unknown avg `10.0664` n `1233`
- 4h: commodity avg `0.0263` n `13`; crypto_alt avg `-2.2299` n `239`; crypto_major avg `-1.1291` n `8`; equity avg `-0.3208` n `168`; fx avg `0.0138` n `6`; index avg `-0.0421` n `27`; metal avg `-0.0242` n `20`; unknown avg `7.127` n `1215`
- 24h: commodity avg `-0.855` n `13`; crypto_alt avg `-3.4183` n `239`; crypto_major avg `-2.8034` n `8`; equity avg `-0.5326` n `168`; fx avg `-0.1579` n `6`; index avg `0.0007` n `27`; metal avg `-0.1223` n `20`; unknown avg `217.3067` n `971`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0816`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
