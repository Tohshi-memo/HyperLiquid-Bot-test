# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T18:02:08.659438+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0141` n `12`; crypto_alt avg `0.4551` n `231`; crypto_major avg `0.3827` n `8`; equity avg `0.1446` n `122`; fx avg `0.0062` n `6`; index avg `0.0288` n `25`; metal avg `0.049` n `20`; unknown avg `-0.0085` n `794`
- 1h: commodity avg `0.0134` n `12`; crypto_alt avg `-0.5061` n `231`; crypto_major avg `-0.5965` n `8`; equity avg `-0.2337` n `122`; fx avg `0.0017` n `6`; index avg `-0.0354` n `25`; metal avg `-0.0852` n `20`; unknown avg `-0.1572` n `794`
- 4h: commodity avg `-0.2248` n `12`; crypto_alt avg `-0.1602` n `231`; crypto_major avg `-0.6145` n `8`; equity avg `0.7673` n `122`; fx avg `-0.0202` n `6`; index avg `0.0954` n `25`; metal avg `-0.1869` n `20`; unknown avg `-0.1334` n `793`
- 24h: commodity avg `-0.2681` n `12`; crypto_alt avg `-1.087` n `231`; crypto_major avg `-0.3167` n `8`; equity avg `-2.5028` n `122`; fx avg `-0.1438` n `6`; index avg `-0.3318` n `25`; metal avg `0.0751` n `20`; unknown avg `3.3884` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
