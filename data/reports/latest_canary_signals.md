# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T15:22:28.919894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0132` n `13`; crypto_alt avg `-0.1433` n `235`; crypto_major avg `-0.083` n `8`; equity avg `0.0204` n `150`; fx avg `0.0068` n `6`; index avg `0.0428` n `26`; metal avg `-0.0234` n `20`; unknown avg `1.5841` n `1074`
- 1h: commodity avg `0.1263` n `13`; crypto_alt avg `-0.428` n `235`; crypto_major avg `-0.258` n `8`; equity avg `-0.0839` n `150`; fx avg `0.0145` n `6`; index avg `0.0377` n `26`; metal avg `0.0276` n `20`; unknown avg `0.2898` n `1074`
- 4h: commodity avg `0.0684` n `13`; crypto_alt avg `-1.1181` n `235`; crypto_major avg `-0.8675` n `8`; equity avg `-0.1588` n `150`; fx avg `-0.0166` n `6`; index avg `-0.0551` n `26`; metal avg `-0.18` n `20`; unknown avg `0.1652` n `1022`
- 24h: commodity avg `1.3338` n `13`; crypto_alt avg `-6.4361` n `235`; crypto_major avg `-4.651` n `8`; equity avg `-2.1647` n `150`; fx avg `-0.1651` n `6`; index avg `-0.4217` n `26`; metal avg `-0.663` n `20`; unknown avg `17.9487` n `988`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1455`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1432`, n `669`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1412`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0954`, n `669`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0932`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `669`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0768`, n `669`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0766`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `669`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0752`, n `669`, weak_sample_signal
