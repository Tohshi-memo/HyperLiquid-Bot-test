# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T18:53:31.781112+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0227` n `12`; crypto_alt avg `-0.1186` n `231`; crypto_major avg `-0.0746` n `8`; equity avg `0.0516` n `122`; fx avg `0.0014` n `6`; index avg `0.0209` n `25`; metal avg `0.0121` n `20`; unknown avg `-0.0535` n `795`
- 1h: commodity avg `0.0687` n `12`; crypto_alt avg `0.1048` n `231`; crypto_major avg `0.0739` n `8`; equity avg `0.2211` n `122`; fx avg `0.006` n `6`; index avg `0.0408` n `25`; metal avg `0.0146` n `20`; unknown avg `-0.011` n `795`
- 4h: commodity avg `0.1191` n `12`; crypto_alt avg `-0.2005` n `231`; crypto_major avg `0.0102` n `8`; equity avg `0.179` n `122`; fx avg `0.0003` n `6`; index avg `0.0452` n `25`; metal avg `0.1147` n `20`; unknown avg `-0.1472` n `795`
- 24h: commodity avg `-0.608` n `12`; crypto_alt avg `-0.3422` n `231`; crypto_major avg `0.9895` n `8`; equity avg `1.5968` n `122`; fx avg `0.0577` n `6`; index avg `0.1805` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.6357` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
