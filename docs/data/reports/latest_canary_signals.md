# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-15T08:07:32.576450+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0063` n `12`; crypto_alt avg `-0.1454` n `233`; crypto_major avg `-0.1463` n `8`; equity avg `-0.1827` n `136`; fx avg `0.0447` n `6`; index avg `-0.0345` n `27`; metal avg `-0.0745` n `20`; unknown avg `-0.1107` n `906`
- 1h: commodity avg `0.0377` n `12`; crypto_alt avg `-0.494` n `233`; crypto_major avg `-0.4011` n `8`; equity avg `-0.2976` n `136`; fx avg `0.0595` n `6`; index avg `-0.0852` n `27`; metal avg `-0.2264` n `20`; unknown avg `3.0922` n `906`
- 4h: commodity avg `0.1752` n `12`; crypto_alt avg `-1.0422` n `233`; crypto_major avg `-1.1567` n `8`; equity avg `-0.73` n `136`; fx avg `0.1302` n `6`; index avg `-0.1755` n `27`; metal avg `-0.3488` n `20`; unknown avg `3.2148` n `876`
- 24h: commodity avg `0.1083` n `12`; crypto_alt avg `-1.857` n `233`; crypto_major avg `-1.248` n `8`; equity avg `-0.2801` n `136`; fx avg `0.2353` n `6`; index avg `-0.1311` n `27`; metal avg `-0.4162` n `20`; unknown avg `4.4689` n `820`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0518`, n `668`, weak_sample_signal
