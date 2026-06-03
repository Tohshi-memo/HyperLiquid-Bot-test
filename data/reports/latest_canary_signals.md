# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T00:37:19.060891+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.46` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0518` n `12`; crypto_alt avg `0.1895` n `228`; crypto_major avg `0.0421` n `8`; equity avg `0.0103` n `69`; fx avg `-0.0029` n `6`; index avg `0.1943` n `23`; metal avg `0.0864` n `18`; unknown avg `0.9353` n `422`
- 1h: commodity avg `-0.2958` n `12`; crypto_alt avg `1.724` n `228`; crypto_major avg `1.3104` n `8`; equity avg `0.2032` n `69`; fx avg `0.0311` n `6`; index avg `0.3874` n `23`; metal avg `0.4411` n `18`; unknown avg `1.3251` n `422`
- 4h: commodity avg `0.4169` n `12`; crypto_alt avg `-0.3024` n `228`; crypto_major avg `-0.229` n `8`; equity avg `-0.0957` n `69`; fx avg `-0.0268` n `6`; index avg `0.2693` n `23`; metal avg `-0.1145` n `18`; unknown avg `0.9333` n `422`
- 24h: commodity avg `0.5944` n `12`; crypto_alt avg `-4.1455` n `228`; crypto_major avg `-5.5111` n `8`; equity avg `1.4422` n `69`; fx avg `0.0559` n `6`; index avg `1.2601` n `23`; metal avg `0.1883` n `18`; unknown avg `-0.4925` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
