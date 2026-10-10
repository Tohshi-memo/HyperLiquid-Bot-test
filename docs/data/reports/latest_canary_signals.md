# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T22:22:27.327024+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1068` n `13`; crypto_alt avg `-0.046` n `235`; crypto_major avg `-0.0087` n `8`; equity avg `-0.0021` n `150`; fx avg `0.0015` n `6`; index avg `0.0002` n `26`; metal avg `-0.0062` n `20`; unknown avg `-0.0539` n `1109`
- 1h: commodity avg `0.1687` n `13`; crypto_alt avg `-0.1603` n `235`; crypto_major avg `-0.0625` n `8`; equity avg `0.0131` n `150`; fx avg `0.003` n `6`; index avg `-0.0028` n `26`; metal avg `0.01` n `20`; unknown avg `-0.195` n `1091`
- 4h: commodity avg `0.2047` n `13`; crypto_alt avg `0.2474` n `235`; crypto_major avg `0.0109` n `8`; equity avg `0.085` n `150`; fx avg `0.0005` n `6`; index avg `0.0123` n `26`; metal avg `0.018` n `20`; unknown avg `-0.3628` n `983`
- 24h: commodity avg `0.1722` n `13`; crypto_alt avg `2.7297` n `235`; crypto_major avg `0.8757` n `8`; equity avg `0.2167` n `150`; fx avg `-0.0039` n `6`; index avg `0.034` n `26`; metal avg `0.0145` n `20`; unknown avg `0.1775` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
