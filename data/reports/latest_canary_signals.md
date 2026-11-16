# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-16T23:52:23.502841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0058` n `13`; crypto_alt avg `0.4044` n `239`; crypto_major avg `0.2582` n `8`; equity avg `0.3612` n `162`; fx avg `-0.0037` n `6`; index avg `0.0547` n `27`; metal avg `0.0876` n `20`; unknown avg `159.9676` n `1266`
- 1h: commodity avg `0.0477` n `13`; crypto_alt avg `-0.1392` n `239`; crypto_major avg `-0.3723` n `8`; equity avg `-0.1251` n `162`; fx avg `-0.0028` n `6`; index avg `0.0144` n `27`; metal avg `0.0682` n `20`; unknown avg `40.7937` n `1264`
- 4h: commodity avg `-0.1014` n `13`; crypto_alt avg `-0.0591` n `239`; crypto_major avg `0.3096` n `8`; equity avg `-0.6304` n `162`; fx avg `-0.0158` n `6`; index avg `-0.0283` n `27`; metal avg `0.0024` n `20`; unknown avg `214.3386` n `1188`
- 24h: commodity avg `-0.9356` n `13`; crypto_alt avg `-0.674` n `239`; crypto_major avg `-0.4445` n `8`; equity avg `-4.5611` n `162`; fx avg `-0.1155` n `6`; index avg `-0.5165` n `27`; metal avg `-0.658` n `20`; unknown avg `505.938` n `995`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1462`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
