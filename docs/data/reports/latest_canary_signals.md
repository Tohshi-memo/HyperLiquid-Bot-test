# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T17:40:18.224486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0251` n `12`; crypto_alt avg `-0.2572` n `231`; crypto_major avg `-0.3427` n `8`; equity avg `0.0131` n `122`; fx avg `0.0101` n `6`; index avg `-0.0076` n `25`; metal avg `0.0057` n `20`; unknown avg `-0.0063` n `793`
- 1h: commodity avg `0.0054` n `12`; crypto_alt avg `0.1781` n `231`; crypto_major avg `-0.0625` n `8`; equity avg `0.0636` n `122`; fx avg `0.0059` n `6`; index avg `0.0076` n `25`; metal avg `-0.0116` n `20`; unknown avg `0.0062` n `793`
- 4h: commodity avg `-0.0252` n `12`; crypto_alt avg `0.6571` n `231`; crypto_major avg `-0.2683` n `8`; equity avg `0.1543` n `122`; fx avg `0.007` n `6`; index avg `0.0266` n `25`; metal avg `0.0219` n `20`; unknown avg `0.5909` n `793`
- 24h: commodity avg `0.0167` n `12`; crypto_alt avg `1.9951` n `231`; crypto_major avg `0.8542` n `8`; equity avg `0.6994` n `122`; fx avg `0.0463` n `6`; index avg `0.0789` n `25`; metal avg `0.0699` n `20`; unknown avg `7.8513` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
