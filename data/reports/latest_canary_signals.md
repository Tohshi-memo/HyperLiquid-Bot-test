# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T07:07:26.555526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0298` n `12`; crypto_alt avg `0.2761` n `234`; crypto_major avg `0.2637` n `8`; equity avg `0.1731` n `137`; fx avg `-0.0178` n `6`; index avg `0.0036` n `27`; metal avg `0.0489` n `20`; unknown avg `7.0361` n `917`
- 1h: commodity avg `-0.1099` n `12`; crypto_alt avg `0.1766` n `234`; crypto_major avg `0.1655` n `8`; equity avg `0.2148` n `137`; fx avg `-0.0391` n `6`; index avg `0.0422` n `27`; metal avg `0.1079` n `20`; unknown avg `6.5298` n `917`
- 4h: commodity avg `-0.105` n `12`; crypto_alt avg `0.3209` n `234`; crypto_major avg `0.2764` n `8`; equity avg `0.5489` n `137`; fx avg `-0.0241` n `6`; index avg `0.0801` n `27`; metal avg `0.0562` n `20`; unknown avg `0.3311` n `881`
- 24h: commodity avg `-0.0306` n `12`; crypto_alt avg `-2.6825` n `234`; crypto_major avg `-2.4745` n `8`; equity avg `0.1062` n `137`; fx avg `0.1369` n `6`; index avg `0.1175` n `27`; metal avg `0.5245` n `20`; unknown avg `18892.3789` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
