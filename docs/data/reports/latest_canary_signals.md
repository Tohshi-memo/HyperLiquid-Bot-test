# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T16:52:28.822366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0259` n `12`; crypto_alt avg `-0.1022` n `230`; crypto_major avg `-0.1122` n `8`; equity avg `0.1049` n `112`; fx avg `0.0038` n `6`; index avg `0.0155` n `25`; metal avg `-0.037` n `20`; unknown avg `-0.0436` n `782`
- 1h: commodity avg `0.0005` n `12`; crypto_alt avg `-0.0894` n `230`; crypto_major avg `-0.2823` n `8`; equity avg `-0.231` n `112`; fx avg `-0.0098` n `6`; index avg `-0.0378` n `25`; metal avg `-0.0251` n `20`; unknown avg `-0.0244` n `782`
- 4h: commodity avg `0.4195` n `12`; crypto_alt avg `-0.2917` n `230`; crypto_major avg `-0.7682` n `8`; equity avg `-0.8606` n `112`; fx avg `0.0172` n `6`; index avg `-0.1703` n `25`; metal avg `-0.3564` n `20`; unknown avg `-0.0039` n `782`
- 24h: commodity avg `0.3942` n `12`; crypto_alt avg `-0.3496` n `230`; crypto_major avg `-0.302` n `8`; equity avg `0.6867` n `112`; fx avg `-0.1414` n `6`; index avg `-0.0293` n `25`; metal avg `0.2286` n `20`; unknown avg `-0.0817` n `765`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
